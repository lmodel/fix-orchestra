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
  A named business idea that ties together the fields, components, groups and messages that express it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraConceptV10  {

  private List<OrchestraConceptMemberV10> fixrMembers;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrName;


}