package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The parties a repository describes and the one-way flows between them.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraActorsV11  {

  private List<OrchestraActorsMemberV11> fixrMembers;
  private OrchestraAnnotationV11 fixrAnnotation;
  private URI xmlBase;


}