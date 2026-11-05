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
  The repeating groups a repository defines.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraGroupsV11  {

  private List<OrchestraGroupV11> fixrGroup;
  private OrchestraEncodingsV11 fixrEncodings;
  private OrchestraAnnotationV11 fixrAnnotation;
  private URI xmlBase;


}