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
  The concepts a repository names.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraConceptsV11  {

  private List<OrchestraConceptV11> fixrConcept;
  private OrchestraAnnotationV11 fixrAnnotation;
  private URI xmlBase;


}